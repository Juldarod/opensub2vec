import React from 'react';
import { Modal, Header } from 'semantic-ui-react';

const About = props => {
    return (
        <Modal dimmer={'blurring'} trigger={props.trigger}>
            <Header icon="book" content="About" />
            <Modal.Content>
                <p>
                    Computational Linguistics has been growing fast last years.
                    Currently, there are linguistic-computational resources that
                    allow us to do vector space model studies of big amounts of
                    text at lexical, syntactic and semantic levels using Machine
                    Learning techniques based on neural networks and provide
                    tools to discover and analyze language regularities in a
                    relatively fast way.
                </p>
                <p>
                    Internet and globalization have brought massive quantities
                    of media productions. Movies and series have flooded
                    television, cinema and online video streaming services
                    worldwide, requiring subtitles in several languages for the
                    population where such services are offered. This situation
                    has made the subtitles topic and their respective
                    translations an essential and relevant issue in the business
                    model of big multinational companies. It is important to
                    find ways to automate and improve machine translation
                    methods since it has become a heavy problem to solve just by
                    human work.
                </p>
                <p>
                    The vector space models mentioned before permit to find
                    linguistic regularities in any language, opening a door to
                    challenge the problem of subtitles. These models are based
                    on contributions made by Distributional Semantics, a
                    research area that studies the Distributional Hypothesis and
                    implements techniques of a probabilistic, neural or mixed
                    nature. This field increments the accuracy of Natural
                    Language Processing tasks as Sentiment Analysis and Text
                    Classification.
                </p>
                <p>
                    In this work, we pretend to show the strengths of
                    Computational Linguistics in concert with distributional
                    semantics advances, vector space models and machine learning
                    in order to explore and compare semantic regularities in
                    bilingual subtitles (English and Spanish) by using
                    neural-natured models as word2vec and fastText, known as
                    Word Embedding models.
                </p>
            </Modal.Content>
        </Modal>
    );
};

export default About;
