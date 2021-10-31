from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
import math


questions = [
'What is an IEP',
'What is an LEA',
'What is IDEA',
'What is FAPE?',
'What is LRE?',
'What is PBIS?',
'What is a BIP?',
'What is RTI?',
'Should I have my child evaluated for special education',
'Can the school district refuse to evaluate my child until he or she goes through the RTI process?',
'Can the school use my private evaluation to expedite the evaluation process? ',
'Is the public school system required to evaluate my child that attends a private school for free?',
'What are the exceptionalities?',
'How long does it take to get my child evaluated?',
'What happens if the parent disagree with the evaluation?',
'If my child is eligible for special education services, how long will it take to start the services?',
'Will I receive a notice about the IEP meeting?',
'Does the school have to tell me who will be attending the meeting?',
'Who are the IEP team members?',
'Are parents equal IEP team members?',
'Who is considered a parent on the IEP team?'
]

answers = [
'IEP is an individualized Education Program that provides a written plan designed to meet the unique needs of the child with an exceptionality.',
'LEA is the local education agency, also referred to as the local school district.',
'IDEA is the Individuals with Disabilities Education Act, the Federal special education law that guarantees FAPE.',
'FAPE is Free Appropriate Public Education, the provision in IDEA to ensure states provide services to eligible students with disabilities. The FREE in FAPE means school services must be provided at public expense, under public supervision and direction, without charge.',
'LRE is least restrictive environment.  LRE is the foundation principle in IDEA that children with disabilities should be educated with their nondisabled peers, to the greatest extent possible. ',
'Positive Behavioral Interventions and Supports is an evidence-based three-tier framework for improving and integrating all of the data, systems, and practicing affecting student outcomes every day.  It’s a way to support everyone – especially students with disabilities – to create the kinds of schools where all students are successful. PBIS isn’t a curriculum you purchase or something you learn during a one-day professional development training. It is a commitment to addressing student behavior through systems change. When it’s implemented well, students achieve improved social and academic outcomes, schools experience reduced exclusionary discipline practices, and school personnel feel more effective.(Center for Positive Behavior Interventions & Supports, a U.S. Department of Education funded Technical Assistance & Dissemination Center)',
'A BIP is a Behavior Intervention Plan.  Many students with disabilities – particularly those with emotional or behavioral disorders, have IEP’s that contain a BIP, which provide individualized procedures to prevent undesirable behaviors or to intervene when those behaviors occur. ',
'The Response to Intervention (RTI) process is a three-tiered approach to providing services and interventions to struggling learners and/or students with challenging behaviors at increasing levels of intensity. Essential components of the process include three tiers of instruction and intervention, use of standard protocols and/or problem-solving methods, and an integrated data collection/assessment system to inform decisions at each tier of instruction/intervention. The process incorporates increasing intensities of instruction and/or intervention that are provided to students in direct proportion to their individual needs. Embedded in each tier is a set of unique support structures or activities that help teachers implement, with fidelity, research-based curricula, instructional practices, and interventions designed to improve student achievement. RTI is designed for use when making decisions in both general and special education, creating a well-integrated system of instruction and intervention guided by student outcome data.',
'If your child is between 3 and 21 and having academic, social, or behavioral problems, you may consider getting your child evaluated. In Louisiana, this is called a 1508 evaluation.  Many struggling learners first go through the School Building Level Committee (SBLC) and receive interventions (RTI) before they are referred for an evaluation. ',
'No, The Office of Special Education Programs under the U.S. Department of Education made it clear a school district cannot delay or deny the evaluation process due to RTI.',
'The school district is required to review all pertinent reports supplied by the parent or an outside agency during the evaluation process.  Normally, these private evaluations don’t meet the requirements of 1508 and therefore the district will conduct their own evaluation. ',
'Yes, if you suspect your child is a child is a disability, the public school system is obligated to evaluate your child under Bulletin 1508 guidelines, at no cost to the parent or private school your child is attending. ',
'The exceptionalities are Autism, Deaf-Blindness, Developmental Delay, Emotional Disturbance, Hearing Impairment, Intellectual Disability, Multiple Disabilities,  Orthopedic Impairment, Other Health Impaired, Specific Learning Disability, Speech or Language Impairment, Traumatic Brain Injury, Visual Impairment',
'The initial evaluation must be conducted within 60 business days of receiving parental consent.',
'The parents of a student with a disability or an exceptionality have a right to obtain an independent educational evaluation (IEE) of the student as described in Chapter 5 of Bulletin 1706.',
'The local education agency (LEA) also referred to as the school district has a maximum of 30 calendar days to complete the IEP/placement document for an eligible student.',
'Yes, a written notice must be provided to the parents of the child.  The notice must be provided in the parents’ native language or shall be given using other means of communication, whenever necessary, to ensure parental understanding. ',
'The notice shall indicate the purpose, time, and location of the IEP Team meeting; who will be in attendance; when a LEA IEP Team member needs to be excused from attending the meeting; the parents\' right to take other participants to the meeting; the student\'s right to participate (when appropriate); and the name of the person in the LEA the parents can contact when they have questions or concerns.',
'At any IEP Team meeting, the following participants shall be in attendance: an officially designated representative of the Local Education Agency (LEA), the student\'s regular education and special education teachers, the student\'s parents, and a person knowledgeable about the student\'s evaluation procedures and results. The student, as well as other individuals the parents and/or LEA may deem necessary, should be given the opportunity to attend. Documentation of attendance is required.'
'Yes, parents are equal participants in the IEP process in discussing the educational and related services needs of the student and in deciding which placement and other services are appropriate. As such, one or both of the student\'s parents should participate in the initial IEP/placement meeting(s). Other team members shall rely on parents to contribute their perspective of the student outside of school. Parental insight about the student\'s strengths and support needs, learning style, temperament, ability to work in various environments, and acquired adaptive skills is of vital importance to the team in making decisions about the student\'s needs and services. The concerns of the parents for enhancing the education of their child shall be documented in the IEP.'
'Parent is defined as a biological or adoptive parent of a child; a foster parent; a guardian, generally authorized to act as the child\'s parent or authorized to make educational decisions for the child, but not the state if the child is a ward of the state; an individual acting in the place of a biological or adoptive parent of a child (including a grandparent, stepparent, or other relative) with whom the child lives or an individual who is legally responsible for the child\'s welfare; or a surrogate parent who has been appointed to act in the child\'s behalf. '
]

print("Hi, how can we help you?")
x = input()

sw = stopwords.words('english')
# print(sw)


question_vectors = []

ranks = []
for idx, question in enumerate(questions):
  l1 = []; l2 = []
  temp = word_tokenize(question)
  question_vectors.append(temp)

  user = word_tokenize(x)

  # remove stop words from the string
  temp_set = {w for w in temp} # if not w in sw}
  print(temp_set)
  user_set = {w for w in user} # if not w in sw}
  print(user_set)

  # form a set containing keywords of both strings
  rvector = temp_set.union(user_set)
  for w in rvector:
      if w in user_set:
          l1.append(1) # create a vector
      else:
          l1.append(0)
      if w in temp_set:
          l2.append(1)
      else:
          l2.append(0)
  c = 0

  # cosine formula
  for i in range(len(rvector)):
          c+= l1[i]*l2[i]
  cosine = c / ((sum(l1)**0.5*(sum(l2))**0.5))
  print("similarity: ", cosine)
  ranks.append((idx, cosine))

ranks.sort(key=lambda y: y[1], reverse=True)
print()
print(ranks)
print()
print("==Answer One:==")
print(answers[ranks[0][0]])
print()
print("==Answer Two:==")
print(answers[ranks[1][0]])
