# Debugging Cloud Deployment
A small-sized startup runs a web server named ws01 in the cloud. One day, when you try to access the website served by ws01, you get an HTTP Error 500. Since your deployment is still in an early stage, you suspect a developer might have used this server to do some testing or run some experiments. Now you need to troubleshoot ws01, find out what's going on, and get the service back to a healthy state.
- HTTP status code meaning
- Check port status with the netstat command
- Manage services with the systemctl command
- Monitor system resources and identify the root cause of an issue