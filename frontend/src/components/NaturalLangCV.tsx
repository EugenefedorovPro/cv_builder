import React from "react";
import { ListGroup, ListGroupItem } from "react-bootstrap";
import { useFetchData } from "../api/UseFetchData";
import { urlNaturalLang } from "../urls";
import { NaturalLangBlockInterface } from "../components/typesComponents";


const NaturalLangCV = () => {
  const name = "Natural languages";
  const { data, loading, error } =
    useFetchData<NaturalLangBlockInterface>(urlNaturalLang);

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

  const { natural_langs, block_names } = data;

  if (!natural_langs || !block_names) {
    return <div>No data on {name}</div>;
  }

  return (
    <>
      <ListGroup>
        <ListGroupItem className="block-name">
          {block_names.natural_lang_name}
        </ListGroupItem>
      </ListGroup>

      <ListGroup>
        <ListGroupItem className="natural-lang-items">
          {natural_langs.map((item, index) => (
            <span key={item.id}>
              <span className="title">{item.natural_lang}</span> - {item.level}
              {index < natural_langs.length - 1 ? " • " : ""}
            </span>
          ))}
        </ListGroupItem>
      </ListGroup>
    </>
  );
};

export default NaturalLangCV;
