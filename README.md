# FileReader
A simple file reader I built to help a friend with an assignment. This file should create/modify three different text files, each containing the different Etot, EKtot, and EPtot values, in the order they appear in in the original parent file. 

## Getting started
After downloading reader.py, and heat.out, simply run the script using the following command.
```
$ python3 reader.py
```

## Troubleshooting
Be sure that both reader.py and heat.out files exist in the same directory. 

## What I Learned
I learned a lot about how to read input from files using python. I also learned a lot about how to use regular expressions.

## Additional Features
I would like to add a couple additional features to this project in the future. Presently, you cannot specify a file to be read from, it only works for 'heat.out', however this functionality will be added, I am just unsure about how I want to implement it exactly. Another feature that I will ponder is the ability to query a file for specific values, aside from Etot, EKtot, and EPtot. The way that the program operates using regular expressions to search the file, there is a foundation for this to be added, again, I just wanted to further consider the exact design implemenation I wanted to use for this feature.
