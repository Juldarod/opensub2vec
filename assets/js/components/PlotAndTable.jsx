import React from 'react';
import {
    Grid,
    Segment,
    Image,
    // Placeholder,
    Table,
    Header,
    Transition,
} from 'semantic-ui-react';

// import blankPicture from '../../static/blankpicture.png';

const PlotAndTable = ({ input, similars, toggle }) => {
    return (
        <Grid columns={2} style={{height:  '549px'}}>
            <Grid.Column verticalAlign="top" widescreen={10}>
                    <Transition.Group animation="zoom">
                {similars.length > 0 && <Segment>

                    {/* <Dimmer active>
                                    <Loader />
                                </Dimmer> */}
                    {/* {similars.length == 0 ? (
                        <Image src={blankPicture} />
                    ) : ( */}
                        <Image
                            src={`http://localhost:5000/plot/${
                                toggle ? 'en' : 'es'
                            }/${input} ${similars
                                .map((el) => el[0])
                                .join(' ')}`}
                                />
                     {/* )} */}
                </Segment>}
                                </Transition.Group>
            </Grid.Column>
            <Grid.Column verticalAlign="top" widescreen={6}>
                <Transition.Group animation="zoom">

                {similars.length > 0 && <Segment>
                    {/* {similars.length == 0 ? (
                        <Placeholder fluid>
                        <Placeholder.Header />
                        <Placeholder.Line />
                        <Placeholder.Line />
                        <Placeholder.Line />
                        <Placeholder.Line />
                        <Placeholder.Line />
                        <Placeholder.Line />
                        <Placeholder.Line />
                        <Placeholder.Line />
                        <Placeholder.Line />
                        </Placeholder>
                    ) : ( */}
                        <Table basic="very" celled>
                            <Table.Header>
                                <Table.Row>
                                    <Table.HeaderCell>Word</Table.HeaderCell>
                                    <Table.HeaderCell>Score</Table.HeaderCell>
                                </Table.Row>
                            </Table.Header>
                            <Table.Body>
                                {similars.map((el) => (
                                    <Table.Row key={el[0]}>
                                        <Table.Cell collapsing>
                                            <Header as="h4">{el[0]}</Header>
                                        </Table.Cell>
                                        <Table.Cell
                                            collapsing
                                            content={String(el[1]).slice(0, 10)}
                                            />
                                    </Table.Row>
                                ))}
                            </Table.Body>
                        </Table>
                    {/* )} */}
                </Segment>}
                                </Transition.Group>
            </Grid.Column>
        </Grid>
    );
};

export default PlotAndTable;
