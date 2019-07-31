import React from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import {
  Container,
  Icon,
  Grid,
  Divider,
  Segment,
  Menu,
  Tab
} from "semantic-ui-react";
import Gear from "../loaders/Gear";
// import Geometry from '../loaders/Geometry';
// import Roller from '../loaders/Roller';
import About from "./About.jsx";
import Contact from "./Contact.jsx";
import PlottingSegment from "./PlottingSegment.jsx";
import ColumnGrid from "./Grid.jsx";

class Dashboard extends React.Component {
  state = {
    // loadedModel: false,
    loadedModel: true
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

  renderLoader = () => {
    return (
      <div
        className="block"
        style={{
          height: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center"
        }}
      >
        <Gear />
        <label style={{ color: "rgba(205, 205, 205, 0.98)" }}>
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
              inverted: true
            }}
            panes={panes}
          />
        </Container>
      </React.Fragment>
    );
  };

  render() {
    const panes = [
      {
        menuItem: "Words",
        render: () => (
          <Tab.Pane>
            (Most Similar)
            <Segment>{}</Segment>
            (Analogies picture)
            <Segment>{}</Segment>
          </Tab.Pane>
        )
      },
      {
        menuItem: "Sentences",
        render: () => (
          <Tab.Pane>
            (sentences in both languages picture)
            <Segment>
              {/* <ColumnGrid columns={2}> */}
              <Grid columns={2} relaxed="very">
                <PlottingSegment model={"English"} />
                <PlottingSegment model={"Spanish"} />
              </Grid>
              <Divider vertical>
                <Icon name="picture" />
              </Divider>
              {/* </ColumnGrid> */}
            </Segment>
            <Segment>
              (sentence translation picture: a sentence in english and its
              translation in spanish)
            </Segment>
            <Segment>
              (wmdistance between original spanish sentence and translated
              sentences)
            </Segment>
          </Tab.Pane>
        )
      }
    ];

    return this.state.loadedModel
      ? this.renderContent(panes)
      : this.renderLoader();
  }
}

export default Dashboard;
