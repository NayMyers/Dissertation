# This document is to keep track of references before they are added to the bibliography and to keep a note of what they will be used for.

## Why SQL?

## Why Vue.js

## Why Jupyter

## Why FLask

## Lit review
Search term = Crop Disease Detection Using Deep Learning

* Using Deep Learning for Image-Based Plant Disease Detection - 2016
  - Uses AlexNet & GoogLeNet
    - GoogLeNet performed best 99.35% on held out test set
  - 54,306 images. 14 crop species and 26 diseases. 38 classes

* Crop Disease Detection Using Deep Learning - 2018
    Omkar Kulkarni
    https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8697390
      - Uses InceptionNetV3 & MobileNet
        - Inception perfomed best.
      - Uses Plantvilla contains 54,306 images & 38 classes. 13 crop species and 26 types of diseases.
      - Achieved 99.74% accuracy with 20% hold out test set.

* Image-Based Tomato Leaves Diseases Detection Using Deep Learning - 2018
  - 9000 images of tomato leaves 5 different diseases
  - Their own CNN architecture
    - 99.84% accuracy on held out test set.

Search term = Plant identification deep learning

*

# Note
  - I want the back-end to be modular in the sense that I am able to choose from multiple CNN's with different functions. For instance:
    - Crop identification
      - In the absence of a label for the crop species, the CNN will be able to identify it.
    - Defect detection
        (disease) || (malnourishment)
    - Taxonomy, eg.
      - Native habitat
      - Soil conditions
      - Latin name
      - Ancestor species
  This will allow the expansion of the functionality. With the end goal to be a website that coalesces the cutting edge in image classification for multiple end goals.
  Is the user
    - Identifying a plant species
    - Identifying a defect
    - Deciding if the plant they have found is a native species?

The application will need to give advice to the user as