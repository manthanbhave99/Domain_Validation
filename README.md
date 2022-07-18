# Domain_Checker
Validate Domain and fetch their favicon using base64 algorithm
Step by step function of this tool
1} First in first we take an input as argument using argparse library.
2} subprocess library helps to execute a command of subfinder.
3} Subfinder is a tool to find all possible subdomains for given input domain. These domain will store in a file named as "subdomains.txt".
4} Open this file in read mode to find domains which are alive. That means find domains whose status code is 2xx. Only these subdomains will store in a file named as "alive.txt".
5} We will storing only these domains who prefers https schema.
# Subfinder Installation
go install https://github.com/projectdiscovery/subfinder
