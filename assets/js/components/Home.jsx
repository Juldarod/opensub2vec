import React from "react";
import { Container, Segment, Menu } from "semantic-ui-react";
import axios from "axios";

class Home extends React.Component {
  state = {
    backendStatus: "",
    activeItem: ""
  };

  // componentDidMount() {
  //     axios
  //         .get('http://localhost:5000')
  //         .then(response => {
  //             console.log(response);
  //             this.setState({ backendStatus: response.data.message });
  //         })
  //         .catch(error => console.log(error.response.data));
  // }

  handleItemClick = (e, { name }) => this.setState({ activeItem: name });

  render() {
    const { activeItem } = this.state;

    return (
      <div id="home">
        <div id="menu">
          <label>Models</label>
          <label>About</label>
          <label>Contact</label>
        </div>
        <div id="landing">
          <text>Opensub2Vec</text>
          <div>
            <div>
              <label>Select a model</label>
              <select />
              <button>Go!</button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Home;
