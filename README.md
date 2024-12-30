Created as an exercise inheritance with Python for assistance building a Mouse Guard campaign.
* Names and Statuses are special Enums.
* Subjects have Names and a list of Statuses.
* Subjects have internal ability to parse, change, and validate their attributes.
* Towns are Subjects, and have a list of Tokens they interact with based on their subclasses.
* Tokens are Subjects, and have a current Town and a set of Towns to Love and Hate.
* Tokens Move and Reset between seasons base on their subclasses; they may also alter Statuses.
