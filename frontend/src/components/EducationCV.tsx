import React from "react";
import { urlEducation } from "../urls";
import { ListGroup, ListGroupItem } from "react-bootstrap";
import { useFetchData } from "../api/UseFetchData";
import type { EducationBlockInterface } from "../components/typesComponents";

const EducationCV = () => {
  const name = "Education";
  const { data, loading, error } =
    useFetchData<EducationBlockInterface>(urlEducation);

  if (loading) {
    return <div> Loading data for {name}...</div>;
  }

  if (error) {
    return (
      <div>
        `Error on fetching {name}: ${error}`
      </div>
    );
  }

  if (!data) {
    return <div>No data on {name}</div>;
  }

  const { education, block_names } = data;

  if (!education || !block_names) {
    return <div>No data on {name}</div>;
  }

  return (
    <>
      <ListGroup>
        <ListGroupItem className="block-name">
          {block_names.education_name}
        </ListGroupItem>
      </ListGroup>

      <ListGroup>
        {education.map((item) => (
          <ListGroupItem key={item.id} className="education-items">
            <span className="title">{item.institution}</span>
            <br />
            {item.start_date} - {item.end_date}
            <br />
            {item.degree_title}
          </ListGroupItem>
        ))}
      </ListGroup>
    </>
  );
};

export default EducationCV;
