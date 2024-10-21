{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "03c888e2-7b20-40c9-8fe9-44db2429f390",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "a = 10\n",
    "b = 20\n",
    "print(a + b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "94e60b7a-2f48-4057-b786-79ce291e5f60",
   "metadata": {},
   "outputs": [
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[2], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;241m10\u001b[39m\u001b[38;5;241m/\u001b[39m\u001b[38;5;241m0\u001b[39m\n",
      "\u001b[0;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "10/0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c04bc648-57ac-4fc7-9756-9259c0bcb55c",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "ZeroDivisionError",
     "evalue": "integer division or modulo by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[3], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;241m10\u001b[39m\u001b[38;5;241m/\u001b[39m\u001b[38;5;241m/\u001b[39m\u001b[38;5;241m0\u001b[39m\n",
      "\u001b[0;31mZeroDivisionError\u001b[0m: integer division or modulo by zero"
     ]
    }
   ],
   "source": [
    "10//0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5e2918e9-a4bc-4d1f-99fe-6862ed1e80b4",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "ZeroDivisionError",
     "evalue": "integer modulo by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[4], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;241m10\u001b[39m\u001b[38;5;241m%\u001b[39m\u001b[38;5;241m0\u001b[39m\n",
      "\u001b[0;31mZeroDivisionError\u001b[0m: integer modulo by zero"
     ]
    }
   ],
   "source": [
    "10%0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "673c71b7-6772-491a-80c3-5f800f368261",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10**0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "63a384e7-1776-428c-9fdd-141c50fd542f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a = 10\n",
    "b = 20\n",
    "print(a < b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "594e9417-5d37-4326-9956-f8348d74e405",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a = 10\n",
    "b = 20\n",
    "print(a <= b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "988cb6d7-c799-4c6a-8a81-e9293af50763",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "a = 10\n",
    "b = 20\n",
    "print(a > b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a72b2ebc-80d9-4e11-9818-98c783c72fc0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "a = 10\n",
    "b = 20\n",
    "print(a >=  b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9df392ff-6aaa-4203-b5a1-c2045337b8f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a < b  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2639fe37-25d8-4717-9bd3-e474480a9805",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'ab' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[11], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m ab \u001b[38;5;241m<\u001b[39m bd\n",
      "\u001b[0;31mNameError\u001b[0m: name 'ab' is not defined"
     ]
    }
   ],
   "source": [
    "ab < bd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "893f0230-a5c2-4d5d-8e5b-4f7996c50c5f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"ab\" < \"ad\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "23b3a34e-3a5f-4919-9a33-01f480f0c0a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "a = 'true'\n",
    "b = 'false'\n",
    "print(a < b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a493654c-bc51-4e6c-8edb-9725be682909",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(10<20<30<40) # if any one is false hen it is false otherwise false"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "73dfeaef-4596-4c7d-9fe3-38b007c545a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print('krish' == 'krish')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "31192764-14d0-4405-a462-c88f533a120b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(10 == 'krish')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "5151d048-9cfd-4935-8682-90f965c0d759",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(10 == 8+2 == 10//1 == 5*2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "27e7f614-5243-4e61-ae41-8998c5276336",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'a' == 97 # one is string arguement and one is number. in python there is no character. here 'a' is string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "5fa0d211-3ba0-49ae-b2ef-f80021a6c598",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10 == 10.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "26239191-2073-4474-9b39-5921096f6ded",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10 == '10'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "efec6d92-7a23-4fd1-9ce4-56fecaa5b03c",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'true' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[24], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;241m1\u001b[39m \u001b[38;5;241m==\u001b[39m true\n",
      "\u001b[0;31mNameError\u001b[0m: name 'true' is not defined"
     ]
    }
   ],
   "source": [
    "1 == true"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "ce2156e0-eb2a-4a93-9c5e-7a4cb639edff",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "cannot assign to literal here. Maybe you meant '==' instead of '='? (1360948295.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[25], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    1 = True\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m cannot assign to literal here. Maybe you meant '==' instead of '='?\n"
     ]
    }
   ],
   "source": [
    "1 = True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "6e9162b2-b552-48fd-809b-cea9e10966b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "1 == True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "ba3600e8-1aa0-41f1-b0dc-3679639f8428",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "True and True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "1af29734-a8ca-432b-8ffe-4e7789c63194",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "False and True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "48e2b11c-0d0b-4f2d-9bea-ce6e9397b097",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "False or True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "5b8271f9-6d8a-4e58-b955-1d2bbaf8c8bc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "False or False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "c9ea9076-cd68-4712-81f7-65174a56973d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "2196fde3-bfd9-43dc-98e8-11f8119cae87",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "ff9641e7-149d-40ae-ac33-7789e7dcf04c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10 and 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "6d99f1bc-440a-4ba6-ae26-824ff0197d88",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "0 and 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "2ea344ac-c0aa-45b9-a14c-1ba2eeb12ba1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'krish'"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "1 and 'krish'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "45e2ab00-dad3-4005-958d-fc54d3c19457",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10 or 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "520fa94f-448f-428b-aa05-c221aeb0939f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "0 or 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "1f1daa29-2fbf-4a64-8755-c130c9146e19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "0293c7a8-0588-4480-a585-00f2cc245f3b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not ''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "73394dfa-c690-4e73-b40c-56cbb376ddc6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 & 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "c7288834-a6c5-493d-84ff-7cdf8a938c75",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 | 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "a2e4e59b-4196-493f-9c6a-dd0cc117d3c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 << 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "e4ced269-fb6e-442a-944c-05dcdc99af79",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 >> 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "62ef4ddd-4580-43ef-b145-d5e2bee3b1ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "20\n",
      "30\n",
      "40\n"
     ]
    }
   ],
   "source": [
    "a,b,c,d = 10,20,30,40\n",
    "print(a)\n",
    "print(b)\n",
    "print(c)\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "1e3c343f-beba-4d06-8c59-17cc6ef89eb0",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "not enough values to unpack (expected 4, got 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[46], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m a,b,c,d \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m10\u001b[39m,\u001b[38;5;241m20\u001b[39m,\u001b[38;5;241m30\u001b[39m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28mprint\u001b[39m(a)\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28mprint\u001b[39m(b)\n",
      "\u001b[0;31mValueError\u001b[0m: not enough values to unpack (expected 4, got 3)"
     ]
    }
   ],
   "source": [
    "a,b,c,d = 10,20,30\n",
    "print(a)\n",
    "print(b)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "c715f662-6921-49a2-a563-13d377cd1f61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20 10\n"
     ]
    }
   ],
   "source": [
    "a = 10\n",
    "b = 20\n",
    "a = a + b\n",
    "b = a - b\n",
    "a = a - b\n",
    "print(a,b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "582315e0-0312-48e7-b524-e52d55da946f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20 10\n"
     ]
    }
   ],
   "source": [
    "a,b = 10,20\n",
    "b,a = a,b\n",
    "print(a,b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "be92e625-0882-4bfa-b8fa-2a8a1790c3c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20 10\n"
     ]
    }
   ],
   "source": [
    "a , b = 10 , 20\n",
    "a = a ^ b\n",
    "b = a ^ b\n",
    "a = a ^ b\n",
    "print(a, b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "29729a4c-61f0-4178-ba76-254d09ef2c76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "a = 30 if 10 < 20 else 40\n",
    "print (a )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "cfe62c63-920a-4049-9b95-9476ca46bdc9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "x = 10\n",
    "y = 10\n",
    "print(x is y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "9b677531-de57-4630-bfea-5cbda50a9ae5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8908168\n",
      "8908168\n"
     ]
    }
   ],
   "source": [
    "x = 10\n",
    "y = 10\n",
    "print(id(x))\n",
    "print(id(y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "662b2896-ae88-437f-b328-19add8b50360",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "x = 10\n",
    "y = 10\n",
    "print(x is not y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "74a83abe-997b-497d-9069-1088dff7651b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "x = 'abc'\n",
    "y = 'cde'\n",
    "print(x is not y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "6b4db7fc-05f2-4896-b85d-0523e6cf4ff3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "x = 'abc'\n",
    "y = 'abc'\n",
    "print(x is not y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "62da9048-feb7-4499-a5c1-91bbdd6c3a97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "l = [1,2,3,4,5]\n",
    "print(2 in l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "5afb14f5-82d1-4ae1-9f94-be21ebe5299b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "l = [1,2,3,4,5]\n",
    "print(2 not in l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96a8f6e7-d2d2-42cc-805e-d46d3669e7af",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
