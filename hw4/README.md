##251: Week 4 Homework
For this homework we were supposed to build a gpfs cluster of 3, and then build a "mumbler" application to produce a markov chain by walking through words based on their associated probability.  
Originally, servers were provisioned for me to accomplish this task, but I got stuck on the mumbler app and decided to come back to it as I was severely behind. Unfortunately, those servers were removed when I came back to the project. Here is what I have done:  

  * configured 3 clusters, "gpfs[1-3]", installed the GPFS program and setup the distributed filesystem
  * started, but never finished, the mumbler app
  * reprovisioned nearly a dozen other triplets of servers on aws using various amis including versions of centos and redhat, but no matter what I do I cant seem to get around an error at the "Make World" step of installation (see makeWorld.log)
  
I have now worked on this countless hours, scowered online resources, and searched all over for a compatible OS without success. While I am now fairly famliar with different linux distros, I have to conceed that I will not be able to get any further on this project.
