import spacy
nlp = spacy.load("en_core_web_sm")
sentences = [
    'Is it possible that I had an allergic reaction to the shot?',
  'Vaccines are scary',
  'My time in Italy was very enjoyable', 'but the vaccine is terrible.',
  'I found the meal to be tasty',
  'The internet was slow.',
  'Our experience was suboptimal'
]
for sentence in sentences:
  doc = nlp(sentence)
  for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
      token.pos_,[child for child in token.children])

for sentence in sentences:
  doc = nlp(sentence)
  descriptive_term = ''
  for token in doc:
    if token.pos_ == 'ADJ':
      descriptive_term = token
  print(sentence)
  print(descriptive_term)

for sentence in sentences:
  doc = nlp(sentence)
  descriptive_term = ''
  for token in doc:
    if token.pos_ == 'ADJ':
      prepend = ''
      for child in token.children:
        if child.pos_ != 'ADV':
          continue
        prepend += child.text + ' '
      descriptive_term = prepend + token.text
  print(sentence)
  print(descriptive_term)

aspects = []
for sentence in sentences:
  doc = nlp(sentence)
  descriptive_term = ''
  target = ''
  for token in doc:
    if token.dep_ == 'nsubj' and token.pos_ == 'NOUN':
      target = token.text
    if token.pos_ == 'ADJ':
      prepend = ''
      for child in token.children:
        if child.pos_ != 'ADV':
          continue
        prepend += child.text + ' '
      descriptive_term = prepend + token.text
  aspects.append({'aspect': target,
    'description': descriptive_term})
print(aspects)
