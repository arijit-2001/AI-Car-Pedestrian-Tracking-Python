# AI-Car-Pedestrian-Detection-Python

created By: Team Xplore

This project was made during a 36hrs OnSpotHackathon organized by Aarohan NIT Durgapur 2021.

PROBLEM STATEMENT:
Self driving vehicle algorithm and code using ML/AI computer vision.
Description : One of the most remarkable applications of Machine Learning in today's world is the self-driving or autonomous car. Design a Machine Learning based self driving vehicle that will improve and enhance the functions and the performance of autonomous cars.


SOLUTION:
We use ML to differentiate between pedestrians and cars so that the self driving vehicle can understand its surrounding and learn to differentiate between the two moving objects i.e, cars and pedestrians to avoid any probability of pedestrian accidents which is a major fear of most critics.

Step 1: We get A lot of Car Images,  
Step2: Make All the images Black and White cause Grayscale images make the algorithm faster. Colour increases the complexity of the model or we can say grey-coloured images are used to simplify the mathematics. For example, one can talk about brightness, contrast, edges, shape, contours, texture, perspective, shadows, and so on, without addressing colour.
Step 3: Train the Algorithm to Detect Cars. Haar features includes edge features, line features, four rectangle features which was used detecting and distinguishing pedestrians and cars. For this, we have developed Haar Cascade xml files based on the concept of Object Detection Algorithm of Machine Learning.
It’s all about matching the feature or shape. If something matches with the above feature, the model will detect it as a pedestrian or a car but to determine the pedestrians and car we have developed a Haar Cascade xml files using machine learning.


FILES :
