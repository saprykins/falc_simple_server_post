from flask import Flask, request, jsonify
import fr_core_news_md

# pip install https://github.com/explosion/spacy-models/releases/download/fr_core_news_md-3.2.0/fr_core_news_md-3.2.0-py3-none-any.whl

app = Flask(__name__)

@app.route("/svo", methods=["POST"])
def get_svo():
    text_received = request.form['text']
    nlp = fr_core_news_md.load()    
    doc = nlp(text_received)
    a_phrase_triplet = '' 
    for token in doc:
        if token.dep_ == "nsubj":
            a_phrase_triplet += token.lemma_ + ' '
        if token.dep_ == "obj":
            a_phrase_triplet += token.lemma_ + ' '
        if token.dep_ == "conj":
            a_phrase_triplet += token.lemma_ + ' '
        if token.dep_ == "advmode":
            a_phrase_triplet += token.lemma_ + ' '
        if token.dep_ == "ROOT":
            a_phrase_triplet += token.lemma_ + ' '
        if token.dep_ == "cop":
            a_phrase_triplet += token.lemma_ + ' '
        if token.dep_ == "amod":
            a_phrase_triplet += token.lemma_ + ' '
        if token.dep_ == "obl":
            a_phrase_triplet += token.lemma_ + ' '
    
    # doc_id_dictionary = {"text": a_phrase_triplet.__str__(encoding='latin1')}
    # doc_id_dictionary = {"text": a_phrase_triplet.encode("utf-8").decode("unicode_escape")}
    doc_id_dictionary = {"text": a_phrase_triplet}
    return jsonify(doc_id_dictionary)
    # return doc_id_dictionary


if __name__ == "__main__":
    app.run(debug=True) # used for debugging
    # app.run()
