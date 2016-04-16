##kluster.me
This was a project for a class in Bioinformatics that gave us freedom to choose a topic of our choice. We dedided to work on a web application that would allow users to select from different clustering algorithms as well as other options for each of the algorithms. This project was our first time using Python as well as our first time using Django, so there is room for improvement. 

This project is a Django application that allows a user to input data via a .csv file and select the clustering algorithm and options of their choice. Upon running the cluster, our application will generate a dendogram that will appear below the clustering menu. The dendrogram is representative of not only of the order of when elements clustered, but the distance between clustered elements accurately depicts the "similarity" between when those clusters happened. 

Our application will also store the results of the cluster to the database and provide a short code that would allow you to pull up that cluster via the "Insert Code" page without recomputing the clustering algorihtm. 

###Clustering Algorithms
Currently our application supports only Single Link Heierarchical Algomerative clustering, with the option of utilizing either Pearson correlation or simple euclidean distance for the distance metric. The backend clustering algorithm is written in Python. 

###Instructions
In its current state, the best way to experience the program is to follow the instructions below to get the server up and running for local use. From there, navigate to the web page and then select "Make Kluster". On this page you will want to have a .csv ready to upload, you can copy and paste the one listed below if you would like to simply see how it works. From here, make sure your linkage type is single and select yes for mapping the kluster. 

For distance metric you can choose from either Euclidean or Pearson, whichever suits you best (both work fine with the sample .csv) and hit "Kluster" to run our algorithm and generate the cluster. The dendrogram will appear below and a code will be given to you. This code can be used to recreate the chart on the "Insert Chart" tab without the alogirthm having to reprocess the clustering.

####Running the server
Running the server for local use and testing is easy, just navigate to BioinformaticsClustering/webapp/clusteringapp and then execute:
```
python manage.py runserver
```
This will get the server up and running adn then you can go on to view the application by opening up your browser and navigating to http://127.0.0.1:8000/

####Format of .CSV
Generally the format of the CSV should look something like this:
```
A,5.67,1.23,3.45,2.34,1.24
B,3.45,5.67,8.9,2.34,5.43
C,1.23,3.45,5.43,2.32,6.87
D,7.65,6.76,1.11,1.2,2.3
E,3.45,5.43,2.34,6.54,3.23
F,7.89,3.23,4.32,3.21,1.1
G,8.97,2.13,4.21,2.31,1
```
The left hand column has the names of each row and then it is a matrix that represents the "differences" between objects. Whatever type of "distances" you are using here should correspond to the type of distance metric you plan on using in the algorithm. 

Note: Although it is a distance matrix mirrored across the diagonal, please refrain from putting a second set of labels along the top axis - our code currently does not handle this properly. 
