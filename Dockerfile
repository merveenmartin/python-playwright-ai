FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    curl unzip git jq sudo ca-certificates \
    python3 python3-pip python3.12-venv \
    openjdk-17-jre \
    libgtk-3-0t64 libnotify4 libnss3 libxss1 libasound2t64 \
    libgbm1 libxshmfence1 \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m agentuser && echo "agentuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

WORKDIR /azp

# Copy locally downloaded Azure DevOps agent package
COPY agent.tar.gz .

# Extract Azure DevOps agent
RUN tar -zxf agent.tar.gz \
    && rm agent.tar.gz

# Install Python dependencies and Playwright browsers
COPY requirements.txt .
RUN pip3 install --break-system-packages -r requirements.txt && \
    playwright install --with-deps

# Copy startup script
COPY start.sh .

# Make script executable
RUN chmod +x start.sh

RUN chown -R agentuser:agentuser /azp

USER agentuser

ENTRYPOINT ["./start.sh"]