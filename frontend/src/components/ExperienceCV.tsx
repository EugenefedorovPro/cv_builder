import React from "react";
import { ListGroup, ListGroupItem } from "react-bootstrap";
import { useFetchData } from "../api/UseFetchData";
import { urlExperience } from "../urls";
import { ExperienceBlockInterface } from "../components/typesComponents";

const ExperienceCV = () => {
  const name = "Experience";
  const { data, loading, error } =
    useFetchData<ExperienceBlockInterface>(urlExperience);

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

  const { experience, block_names } = data;

  if (!experience || !block_names) {
    return <div>No data on {name}</div>;
  }

  return (
    <>
      <ListGroup>
        <ListGroupItem className="block-name">
          {block_names.experience_name}
        </ListGroupItem>
      </ListGroup>

      <ListGroup>
        {experience.map((item) => (
          <ListGroupItem key={item.id} className="experience-items">
            <span className="title">{item.company}</span>
            <br />
            <ul>
              <li>
                <span className="title">{block_names.exp_period_title}</span>{" "}
                {item.start_date} - {item.end_date ? item.end_date : "current"}
                <br />
              </li>
              <li>
                <span className="title">{block_names.position_title}</span>{" "}
                {item.position}
                <br />
              </li>
              <li>
                <span className="title">{block_names.achievements_title}</span>
                <br />
                <span>{item.achievements}</span>
              </li>
            </ul>
          </ListGroupItem>
        ))}
      </ListGroup>
    </>
  );
};

export default ExperienceCV;
