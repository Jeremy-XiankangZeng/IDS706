# ZLLZ Online Sentiment Analysis Application

Sentiment analysis is a text mining field that analyzes and extracts people's opinion towards different topics through detecting the contextual polarization of the text. With the increase in popularity of social media, sentiment analysis can be widely applied to customer reviews and survey responses. Through grasping the sentiments of the general public, companies and organizations are able to make effective decisions or business plans. You can click [HERE](http://zllz-project-test11.eba-akcgpnm3.us-east-2.elasticbeanstalk.com/) to view the website.

## Application Architecture
For the front-end, we used html, css and javascript to build the architecture of our website. Then we created a flask app for a real-time inference interactive model, which takes the user input text and returns the sentiment analysis prediction result back to the user. We wrapped up all of our codes and packages needed in the docker and run our flask app in AWS Elastics Beanstalk. This flask app triggers the lambda function everytime the user clicks 'predict', which will save the input text data in our DynamoDB, and send it to the AWS NLP comprehend model. Finally it will return the result back to the website.

Below is our workflow chart for the whole data pipeline.

![](https://github.com/Jeremy-XiankangZeng/IDS706/blob/main/app/static/img/Application%20Workflow.png)


## Toolkits
Tools: Docker, Git, Flask  
Language: Python, shell, HTML/CSS, Javascript  
AWS related: IAM, Cloud9, Comprehend, Lambda, DynamoDB  

## Team Member
Zihao Lin: zl293@duke.edu    
Yuwei Zhang: yz667@duke.edu  
Xiankang Zeng: xz301@duke.edu  
Qingying Luo: ql111@duke.edu  

## Website

http://zllz-project-test11.eba-akcgpnm3.us-east-2.elasticbeanstalk.com/