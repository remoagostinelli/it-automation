# Debugging Puppet Installation
One of your coworkers of the IT team has recently set up a Puppet installation, but it doesn't seem to be doing its job. So, you're asked to debug the profile class, which is supposed to append a path to the environment variable $PATH. But it's somehow misbehaving and causing the $PATH variable to be broken. You'll need to locate the issue and fix it.
- Check out what Puppet rules look like
- Run the Puppet agent locally
- File permissions represented by numbers
- Scripts under /etc/profile.d/ perform startup tasks
- Set up your own environment variables and append them strings