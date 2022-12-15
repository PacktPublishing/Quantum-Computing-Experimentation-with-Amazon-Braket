
### Get this product for $5

<i>Packt is having its biggest sale of the year. Get this eBook or any other book, video, or course that you like just for $5 each</i>


<b><p align='center'>[Buy now](https://packt.link/9781800565265)</p></b>


<b><p align='center'>[Buy similar titles for just $5](https://subscription.packtpub.com/search)</p></b>


# Quantum Computing Experimentation with Amazon Braket

<a href="https://www.packtpub.com/product/quantum-computing-experimentation-with-amazon-braket/9781800565265?utm_source=github&utm_medium=repository&utm_campaign=9781800565265"><img src="https://static.packt-cdn.com/products/9781800565265/cover/smaller" alt="Book Name" height="256px" align="right"></a>

This is the code repository for [Quantum Computing Experimentation with Amazon Braket](https://www.packtpub.com/product/quantum-computing-experimentation-with-amazon-braket/9781800565265?utm_source=github&utm_medium=repository&utm_campaign=9781800565265), published by Packt.

**Explore Amazon Bracket quantum computing to solve combinatorial optimization problems**

## What is this book about?
Amazon Braket is a cloud-based pay-per-use platform for executing quantum algorithms on different types of cutting-edge quantum computers and simulators. This single platform is ideal for developing robust, high-performance applications with the latest quantum devices.

This book covers the following exciting features: 
* Explore the features and uses of the Amazon Braket console and components
* Discover benefits of quantum computing devices available on Amazon Braket, including gate quantum computers, annealer, and simulators
* Recognize which type of quantum device is the best fit for specific use cases and scaling
* Develop your own code from a basic set of use cases dealing with real-world optimization problems
* Understand the capabilities and limitations of current quantum computing technologies

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1800565267) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>


## Instructions and Navigations
All of the code is organized into folders. For example, Chapter03.

Anyone running the code takes responsibility for any Amazon charges, and to review the code in detail to understand device costs and how many times a device is called from within a function to calculate total costs. Any accidental costs are not the responsibility of Packt Publishing or the Author.

Overview of Amazon Braket Pricing:https://aws.amazon.com/braket/pricing/
 
Tracking costs through code and setting limits:
https://docs.aws.amazon.com/braket/latest/developerguide/braket-pricing.html
 
AWS free tier for first time users
https://aws.amazon.com/braket/pricing/?loc=ft#AWS_Free_Tier


The code will look like the following:
```
from braket.aws import AwsDevice, AwsQuantumTask
from braket.circuits import Circuit
from braket.devices import LocalSimulator
# Set the number of shots 
n_shots = 10
# Use SV1 device
device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")
# Set the S3 bucket and folder name
my_bucket = "[bucket Name]" 
my_prefix = "[Folder Name]" 
s3_folder = (my_bucket, my_prefix)
# Define the quantum circuit
circ = Circuit().h(0).cnot(0, 1)
print(circ)
```

**Following is what you need for this book:**
This book is suitable for IT practitioners, architects, and developers looking to bring the power of quantum computing to their organizations. If you are a VP of IT, CIO, VP of architecture, chief architect, solution architect, actuarial fellow, or a developer already working on other AWS services such as AWS Lambda and EC2. You'll find this book useful in exploring how to leverage Amazon Braket for real-world use cases and useful to move your organization towards this emerging technology. Familiarity with the basics of quantum computing and Python is required.

With the following software and hardware list you can run all code files present in the book (Chapter 1-13).

### Software and Hardware List

| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| 1-13        | Python and Jupyter Notebook                   | Windows |
| 1-13       | Amazon Braket SDK and Boto3             | Windows |
| 1-13        | D-Wave Ocean SDK             | Windows |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://packt.link/4tYx3).


### Related products <Other books you may enjoy>
* Quantum Computing in Practice with Qiskit® and IBM Quantum Experience® [[Packt]](https://www.packtpub.com/product/quantum-computing-in-practice-with-qiskit-and-ibm-quantum-experience/9781838828448?utm_source=github&utm_medium=repository&utm_campaign=9781838828448) [[Amazon]](https://www.amazon.com/dp/1838828443)

* Essential Mathematics for Quantum Computing [[Packt]](https://www.packtpub.com/product/essential-mathematics-for-quantum-computing/9781801073141?utm_source=github&utm_medium=repository&utm_campaign=9781801073141) [[Amazon]](https://www.amazon.com/dp/1801073147)

* Dancing with Python [[Packt]](https://www.packtpub.com/product/dancing-with-python/9781801077859) [[Amazon]](https://www.amazon.com/dp/1801077851)

* Dancing with Qubits [[Packt]](hhttps://www.packtpub.com/product/dancing-with-qubits/9781838827366) [[Amazon]](https://www.amazon.com/dp/1838827366)

## Get to Know the Author
**Alex Khan**
is an advisor, entrepreneur, and educator in quantum computing. He currently heads QuantFi USA operations and is the CEO of ZebraKet, an Ontario based quantum startup in supply chain optimization. Alex has been working in quantum computing since 2018 and was the CPO at Chicago Quantum where he co-authored papers on portfolio optimization using D-Wave. He continues to be an advisor at QuSecure. As a Corporate Faculty, he teaches undergraduate to graduate level courses in quantum computing at Harrisburg University. He has participated in multiple hackathons, advised on a research paper on COVID optimization using quantum annealing, developed solutions for VR game optimization and NLP using D-Wave and has presented introductory topics in quantum computing at quantum meetups including using D-Wave and IonQ through Amazon Braket. Alex has over 20 years of experience providing IT solutions, developing products, and managing large IT initiatives in the healthcare and insurance industry. He is an engineering/physics dual major and received his BSME from Purdue University, MSME from KSU, MBA with Health Sector Management from Duke University and a certificate in quantum computing from MIT|xPro.

### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781800565265">https://packt.link/free-ebook/9781800565265 </a> </p>