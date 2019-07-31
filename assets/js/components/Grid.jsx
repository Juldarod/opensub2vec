import React, { Fragment } from "react";
import { Divider, Grid, Icon } from "semantic-ui-react";

const ColumnGrid = props => {
  const { columns } = props;

  return (
    <Fragment>
      <Grid columns={columns} relaxed="very">
        {props.children}
      </Grid>
      <Divider vertical>
        <Icon name="picture" />
      </Divider>
    </Fragment>
  );
};

export default ColumnGrid;
