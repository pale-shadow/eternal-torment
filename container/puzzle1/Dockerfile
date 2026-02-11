# Use the official Alpine image from the Docker Hub
FROM alpine:latest

# Set the working directory
WORKDIR /app

# Install any necessary packages (optional, as Alpine comes with `ash` by default)
RUN apk add --no-cache

# Copy files from the current directory to the container
COPY . .

# Command to run when the container starts
CMD ["ash"]

