# 0x09. Web infrastructure design
## General
draw a diagram covering the web stack you built with the sysadmin/devops track projects
explain what each component is doing
explain system redundancy
Know all the mentioned acronyms: LAMP, SPOF, QPS
### LAMP (Linux, Apache, MySQL, PHP/Perl/Python) 
is an acronym denoting one of the most common solution stacks for many of the web's most popular applications. 
However, LAMP now refers to a generic software stack model and its components are largely interchangeable.
### Single point of failure (SPOF)
is a part of a system that, if it fails, will stop the entire system from working.
SPOFs are undesirable in any system with a goal of high availability or reliability, be it a business practice, software application, or other industrial system.
### QPS
Queries per second (QPS) is a common measure of the amount of search traffic an information retrieval system, such as a search engine or a database, receives during one second.
The term is used more broadly for any request–response system, more correctly called requests per second (RPS).
High-traffic systems must watch their QPS in order to know when to scale the system to handle more load.
## File Descriptions
Each file contains a link to an image hosted on Imgur. These images are based on the following requirements:

### 0-simple_web_stack
On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via www.foobar.com. Start your explanation by having a user wanting to access your website.
You must use:

* 1 physical server
** 1 web server (Nginx)
1 application server
1 application files (your code base)
1 database (MySQL)
1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8
### 1-distributed_web_infrastructure
On a whiteboard, design a three servers web infrastructure that host the website www.foobar.com.
You must add to 0-simple_web_stack:

2 physical servers
1 web server (Nginx)
1 application server
1 load-balancer (HAproxy)
1 application files (your code base)
1 database (MySQL)
### 2-secured_and_monitored_web_infrastructure
On a whiteboard, design a three servers web infrastructure that host the website www.foobar.com, it must be secured, serve encrypted traffic and be monitored.
You must add to 1-distributed_web_infrastructure:

3 firewalls
1 SSL certificate to serve www.foobar.com over HTTPS
3 monitoring clients (data collector for Sumologic or other monitoring services)
3-scale_up
You must add to 2-secured_and_monitored_web_infrastructure:

1 physical server
1 load-balancer (HAproxy) configured as cluster with the other one
Split components (web server, application server, database) with their own server
## Authors
Kalkidan Demes
Amanuel Sisay
Heyeman Urgessa 
