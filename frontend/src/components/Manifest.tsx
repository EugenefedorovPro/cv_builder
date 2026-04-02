import React from "react";
import { ListGroup, ListGroupItem } from "react-bootstrap";
import { useFetchData } from "../api/UseFetchData";
import { ManifestBlockInterface } from "../components/typesComponents";

const ManifestCV = () => {
  const name = "Manifest";
  const url: string = "http://localhost:8002/manifest/";
  const { data, loading, error } = useFetchData<ManifestBlockInterface>(url);

  if (loading) {
    return <div> Loading data for {name}...</div>;
  }

  if (error) {
    return (
      <div>
        Error on fetching {name}: {error}
      </div>
    );
  }

  if (!data) {
    return <div>No data on {name}</div>;
  }

  const { manifest, block_names } = data;

  if (!manifest || !block_names) {
    return <div>No data on {name}</div>;
  }

  return (
    <ListGroup>
      <ListGroupItem>
        <span className="manifest">{manifest.manifest_text}</span>
      </ListGroupItem>
    </ListGroup>
  );
};

export default ManifestCV;

