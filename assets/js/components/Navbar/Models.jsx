import React from 'react';
import { Modal, Header } from 'semantic-ui-react';

const Models = props => {
    return (
        <Modal dimmer={'blurring'} trigger={props.trigger}>
            <Header icon="cogs" content="Models" />
            <Modal.Content>
                <p>
                    Word embeddings is a collective name associated to language
                    modeling techniques and natural language processing features
                    learning where words are mapped into vectors of real
                    numbers. The objective of word embeddings is to improve the
                    ability of neural networks to learn from text data by
                    representing this data into vectors where similar meaning in
                    words would have a similar numerical representation.
                </p>
                <h3>word2vec</h3>
                <p>
                    This model was proposed in the paper Efficient Estimation of
                    Word Representations in Vector Space by Tomas Mikolov team
                    at Google. In this paper, two architectures were proposed to
                    compute continuous word representations from words in very
                    large datasets: CBOW and Skip-gram. They both use a shallow
                    neural network and back-propagation to learn.
                </p>
                <p>
                    The former is called Continuous Bag-of-Words Model or CBOW.
                    It considers each word context as the input and attempts to
                    make a prediction of the word according to the context. The
                    later (Skip-gram) is considered as the counterpart of CBOW
                    since it takes the words as the input to predict the
                    context. Both architectures are quite similar; however,
                    Skip-gram strives to maximize classification of a word by
                    considering another word in the same sentence, rather than
                    making predictions of the current word based on the context.
                    The following graph represents these architectures
                    functioning.
                </p>
                <h3>fastText</h3>
                <p>
                    Given that previous models used to ignore the morphological
                    information of words by assigning a different vector to each
                    word -something very limiting especially for languages with
                    very complex vocabulary and weird words- the fastText model
                    technique was suggested. It is derived from the skip-gram
                    model in which each vector is associated to an n-gram
                    character in a word, so that the total word is the sum of
                    these associated vectors. In this model, each word is
                    symbolized as a bag of n-grams characters plus the word
                    itself. They are also very helpful at providing the meaning
                    of shorter words and capturing the meaning of affixes.
                </p>
            </Modal.Content>
        </Modal>
    );
};

export default Models;
