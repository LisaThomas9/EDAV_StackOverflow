{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "d ={}\n",
    "ctr = 0\n",
    "with open('data.csv', 'r', encoding=\"utf8\") as csvFile:\n",
    "    reader = csv.reader(csvFile)\n",
    "    r = 0\n",
    "    for row in reader:\n",
    "        if r!= 0:\n",
    "            ctr +=1\n",
    "            taglist = row[4]\n",
    "            user = row[7]\n",
    "            reputation = row[8]\n",
    "            \n",
    "            #print(ctr)\n",
    "            #print(row)\n",
    "            \n",
    "            #print(year)\n",
    "            if len(taglist) ==2 :\n",
    "                continue\n",
    "            else :    \n",
    "                taglist = taglist.replace(\"[\", \"\")\n",
    "                taglist = taglist.replace(\"]\", \"\")\n",
    "                if \"'\" in taglist :\n",
    "                    taglist = taglist.replace(\"'\", \"\")\n",
    "                    taglist = taglist.replace(\" \", \"\")\n",
    "                tag = taglist.split(\",\")                  \n",
    "                for i in range(len(tag)):\n",
    "                    tag[i] = tag[i].strip()\n",
    "                    if (tag[i] , user, reputation) in d:\n",
    "                        d[(tag[i] , user, reputation)] += 1\n",
    "                    else :\n",
    "                        d[(tag[i] , user, reputation)] = 1\n",
    "                        \n",
    "        r = r+1\n",
    "        \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "with open(\"tags_user.csv\",\"w\",  encoding='utf8') as outfile5:\n",
    "#outfile5 = open(\"tags_user.csv\",\"w\",  encoding='utf8')\n",
    "    writer5 = csv.writer(outfile5, delimiter=\",\")\n",
    "    writer5.writerow([\"Tag\",\"User\", \"Reputation\", \"Counts\"])\n",
    "    for i in d :\n",
    "        writer5.writerow([i[0], i[1], i[2], d[i] ])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "d ={}\n",
    "ctr = 0\n",
    "with open('data.csv', 'r', encoding=\"utf8\") as csvFile:\n",
    "    reader = csv.reader(csvFile)\n",
    "    r = 0\n",
    "    for row in reader:\n",
    "        if r!= 0:\n",
    "            ctr +=1\n",
    "            taglist = row[4]\n",
    "            ques = row[0]\n",
    "            votes = row[1]\n",
    "            \n",
    "            #print(ctr)\n",
    "            #print(row)\n",
    "            \n",
    "            #print(year)\n",
    "            if len(taglist) ==2 :\n",
    "                continue\n",
    "            else :    \n",
    "                taglist = taglist.replace(\"[\", \"\")\n",
    "                taglist = taglist.replace(\"]\", \"\")\n",
    "                if \"'\" in taglist :\n",
    "                    taglist = taglist.replace(\"'\", \"\")\n",
    "                    taglist = taglist.replace(\" \", \"\")\n",
    "                tag = taglist.split(\",\")                  \n",
    "                for i in range(len(tag)):\n",
    "                    tag[i] = tag[i].strip()\n",
    "                    if (tag[i] , ques, votes) in d:\n",
    "                        d[(tag[i] , ques, votes)] += 1\n",
    "                    else :\n",
    "                        d[(tag[i] , ques, votes)] = 1\n",
    "                        \n",
    "        r = r+1\n",
    "        \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "with open(\"tags_votes.csv\",\"w\",  encoding='utf8') as outfile5:\n",
    "#outfile5 = open(\"tags_user.csv\",\"w\",  encoding='utf8')\n",
    "    writer5 = csv.writer(outfile5, delimiter=\",\")\n",
    "    writer5.writerow([\"Tag\",\"Ques\", \"Votes\", \"Counts\"])\n",
    "    for i in d :\n",
    "        writer5.writerow([i[0], i[1], i[2], d[i] ])\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "py36",
   "language": "python",
   "name": "py36"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
