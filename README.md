# Flask-Backend-For-BankNote-Identification

## Work Done
A Flask app was developed, and then it was deployed on an AWS EC2 Linux server. To ensure the proper working and performance of the Flask app, two additional components were used: Gunicorn and Nginx.

Flask App Development: The Flask app was developed using the Flask framework, which is a popular Python web framework. The Flask app contains the necessary routes, views, and business logic to handle HTTP requests and generate responses.

AWS EC2 Linux Server: An Amazon EC2 instance running Linux was set up on AWS. This server provides the hosting environment for deploying the Flask app.

Gunicorn: Gunicorn (Green Unicorn) is a WSGI (Web Server Gateway Interface) HTTP server for Python web applications. It acts as a bridge between the web server and the Flask app. Gunicorn manages multiple worker processes to handle concurrent requests and provides performance improvements.

Nginx: Nginx is a high-performance web server and reverse proxy server. It acts as a front-end server and handles incoming requests. Nginx is responsible for routing requests to the Flask app through Gunicorn. It can also handle static file serving, load balancing, and caching.

Deployment Steps:

Install Gunicorn: Gunicorn needs to be installed on the EC2 server. This can be done using pip, the Python package manager.

Configure Gunicorn: Set up a Gunicorn configuration file that specifies the Flask app's entry point, the number of worker processes, and other relevant settings.

Install Nginx: Install Nginx on the EC2 server using the package manager available for the Linux distribution.

Configure Nginx: Set up an Nginx configuration file that defines the server blocks, routes, and proxy pass configurations. This ensures that Nginx forwards requests to the Gunicorn server.

Start Gunicorn and Nginx: Start Gunicorn to run the Flask app using the configured Gunicorn settings. Also, start Nginx to handle incoming requests and proxy them to Gunicorn.

Configure Security Groups and Firewall: Configure the security groups and firewall settings of the EC2 instance to allow incoming HTTP/HTTPS traffic on the specified ports.

Domain and DNS Configuration: If you have a custom domain, configure the DNS settings to point to the public IP address of your EC2 instance.

With these steps, the Flask app is deployed on the AWS EC2 Linux server, and Gunicorn and Nginx are used to ensure proper functioning and performance of the app. Nginx acts as a reverse proxy and handles the incoming requests, while Gunicorn runs the Flask app and manages the worker processes

## Screenshot of working flask api
<img width="628" alt="Screenshot 2023-05-27 at 3 02 41 PM" src="https://github.com/karan-pawar-09/Flask-Backend-For-BankNote-Identification/assets/70064211/760ff4b2-2847-4d42-a8a1-0e902756e34d">

## best_model.h5 link
https://drive.google.com/file/d/1yyM23G7Hvs7K-Q7Z23jBctxSi_2e9Bl5/view?usp=share_link

## colab notebook link
https://colab.research.google.com/drive/1avp-iSzpe_AiGj3UAuUpEwMBoqJltOon?usp=sharing
