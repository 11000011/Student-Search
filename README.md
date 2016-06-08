# Student-Search
A python script to get data of any student in IIT Kanpur with roll number.
If you are not from there, this of no use because this only works from inside
the campus.

## Requirements

`python3` - Installed on most modern linux distributions
If not Installed, can be installed using:
``` shell
# Debian, Ubuntu or other Debian based distros
sudo apt-get install python3
# Arch Linux
pacman -Syu python3
# Red-Hat based distributions
rpm install python3
```

## Usage
From terminal, give the script execution access by:

``` shell
chmod +x search.py
```

Now, the script can be run by :

``` shell
./search.py
```

You can use `createdb.py` by
``` shell
chmod +x createdb.py
./createdb.py
```

Create Database accepts a starting and ending range of roll numbers for generating an
sqlite database which can be easily browsed and queried by various applications.

If the person with that specific roll number does not exist, createdb shows a failure message.

There is a time interval of 0.3 seconds so that the server doesn't think this is a ddos attack.

### Note
We believe we can obtain information using this which should not be public - Such as someone's **home address
and phone numbers**. *This data should not be public*, even if it is to the iitk junta. This a security exploit in
the system, or maybe a known fact.

In any case, this data should not be misused/used without the approval of the
persons involved.

We managed to find this exploit in our second week here (no bragging) when we didn't even know about
security exploits or information security. So someone sufficiently knowledgeable in infosec might even be able to extract more
data???
