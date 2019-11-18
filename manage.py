# setup a new openshift environment including images from setup.yaml file

from time import time as timestamp
import sys,os
import yaml
import requests
from jinja2 import FileSystemLoader, Environment

# read in file
portal_def = yaml.load(open('setup.yaml'))[0]

timestamp = str(int(timestamp()))
 
# load jinja2 templates
file_loader = FileSystemLoader("docker_templates")
env = Environment(loader = file_loader)
#print(timestamp)
#print(template.render())
# create new target dir for all our files
target_dir = "./RUN%s" % (timestamp)
os.mkdir(target_dir)



# loop through our zone definitions
for zone in portal_def["zones"]:
   # for each zone create controlling namespace - which makes all connections (docker image) - for each zone
   controller_dir = zone["zone"] + "_controller"
   os.mkdir(target_dir + "/" + controller_dir)

   # copy this zone definition to new target dir as we will need it there
   with open(target_dir + "/" +controller_dir + "/my_own_zone.yaml", "w") as my_file: # Use file to refer to the file object
      # add srvs domain to zone as we will need this
      zone["srvs_domain"] = portal_def["srvs_domain"] 
      yaml.dump(zone, my_file, default_flow_style=False)

   # for each member of zone create a namespace as well
   for namespace in zone["member_ns"]:
     with open(target_dir + "/" +controller_dir + "/ns_" + namespace["name"] + ".yaml", "w") as my_file: # Use file to refer to the file object
        # add srvs domain to zone as we will need this
        namespace["srvs_domain"] = portal_def["srvs_domain"] 
        yaml.dump(namespace, my_file, default_flow_style=False)
       
       
