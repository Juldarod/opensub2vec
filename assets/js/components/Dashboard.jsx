import React from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import {
    Button,
    Container,
    Image,
    Input,
    Icon,
    Grid,
    Divider,
    Segment,
    Menu,
    Tab,
    Transition,
} from 'semantic-ui-react';
import Gear from '../loaders/Gear';
// import Geometry from '../loaders/Geometry';
// import Roller from '../loaders/Roller';
import About from './About.jsx';
import Contact from './Contact.jsx';
import PlottingSegment from './PlottingSegment.jsx';

class Dashboard extends React.Component {
    state = {
        // loadedModel: false,
        loadedModel: true,
        englishMSimilarVisible: false,
        englishMSimilarPhraseInput: '',
        englishMSimilarPhrase: '',
        spanishMSimilarVisible: false,
        spanishMSimilarPhraseInput: '',
        spanishMSimilarPhrase: '',
    };

    componentDidMount() {
        const { model } = this.props.match.params;

        // axios
        //     .get(
        //         `http://localhost:5000/model/load/${model}` /* , {
        //         onDownloadProgress: function(e) {
        //             console.log(e);
        //         },
        //     } */
        //     )
        //     .then(response => {
        //         // console.log(response);
        //         this.setState({ loadedModel: true });
        //     })
        //     .catch(error => console.log(error.response));
    }

    onEnglishSearchChange = e => {
        this.setState({ englishMSimilarPhraseInput: e.target.value });
    };

    onEnglishSearchClick = async () => {
        await this.setState({ englishMSimilarVisible: false });
        await this.setState({
            englishMSimilarPhrase: this.state.englishMSimilarPhraseInput,
        });
        await this.setState({ englishMSimilarVisible: true });
    };

    onSpanishSearchChange = e => {
        this.setState({ spanishMSimilarPhraseInput: e.target.value });
    };

    onSpanishSearchClick = async () => {
        await this.setState({ spanishMSimilarVisible: false });
        await this.setState({
            spanishMSimilarPhrase: this.state.spanishMSimilarPhraseInput,
        });
        await this.setState({ spanishMSimilarVisible: true });
    };

    renderLoader = () => {
        return (
            <div
                className="block"
                style={{
                    height: '100%',
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'center',
                    alignItems: 'center',
                }}
            >
                <Gear />
                <label style={{ color: 'rgba(205, 205, 205, 0.98)' }}>
                    Loading models...
                </label>
            </div>
        );
    };

    // renderImage = phrase => {
    //     return <Image src={`http://localhost:5000/plot/en/${phrase}`} />;
    // };

    renderContent = panes => {
        return (
            <React.Fragment>
                <Container id="home-menu">
                    <Menu secondary>
                        <Link to="/">
                            <Menu.Item name="Home" />
                        </Link>
                        <Menu.Menu position="right">
                            <About trigger={<Menu.Item name="About" />} />
                            <Contact trigger={<Menu.Item name="Contact" />} />
                        </Menu.Menu>
                    </Menu>
                </Container>
                <Container>
                    <Tab
                        id="tabs"
                        menu={{
                            secondary: true,
                            pointing: true,
                            inverted: true,
                        }}
                        panes={panes}
                    />
                </Container>
            </React.Fragment>
        );
    };

    render() {
        const {
            englishMSimilarVisible,
            englishMSimilarPhrase,
            spanishMSimilarVisible,
            spanishMSimilarPhrase,
        } = this.state;
        const panes = [
            {
                menuItem: 'Words',
                render: () => (
                    <Tab.Pane>
                        (Most Similar)
                        <Segment>{}</Segment>
                        (Analogies picture)
                        <Segment>{}</Segment>
                    </Tab.Pane>
                ),
            },
            {
                menuItem: 'Sentences',
                render: () => (
                    <Tab.Pane>
                        (sentences in both languages picture)
                        <Segment>
                            <Grid columns={2} relaxed="very">
                                <PlottingSegment
                                    model={'English'}
                                    onSearchChange={this.onEnglishSearchChange}
                                    onSearchClick={this.onEnglishSearchClick}
                                    visible={englishMSimilarVisible}
                                    input={englishMSimilarPhrase}
                                />
                                <PlottingSegment
                                    model={'Spanish'}
                                    onSearchChange={this.onSpanishSearchChange}
                                    onSearchClick={this.onSpanishSearchClick}
                                    visible={spanishMSimilarVisible}
                                    input={spanishMSimilarPhrase}
                                />
                            </Grid>
                            <Divider vertical>
                                <Icon name="picture" />
                            </Divider>
                        </Segment>
                        <Segment>
                            (sentence translation picture: a sentence in english
                            and its translation in spanish)
                        </Segment>
                        <Segment>
                            (wmdistance between original spanish sentence and
                            translated sentences)
                        </Segment>
                    </Tab.Pane>
                ),
            },
        ];

        return this.state.loadedModel
            ? this.renderContent(panes)
            : this.renderLoader();
    }
}

export default Dashboard;
