{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fc7edcee-ae02-4299-817a-a80f9f5382d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-05-05 04:48:27.374 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /Users/yangliu/opt/anaconda3/lib/python3.9/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# Load the dataset\n",
    "data = pd.read_csv(\"new_df.csv\")\n",
    "\n",
    "# Display the dataset in a Streamlit app\n",
    "st.write(\"My Dataset\", data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01073960-c6fe-42d1-8da0-d77665f0f23c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
