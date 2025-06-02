import React from "react";
import {ListGroup, ListGroupItem} from "react-bootstrap";
import {useFetchData} from "../api/UseFetchData";

type BlockNameObject = {
    block_name: string;
}

interface ManifestItemInterface {
    id: number;
    manifest_text: string;
}

const ManifestCV = () => {
    const url: string = "http://localhost:8002/manifest/";
    const {data, loading, error} = useFetchData<[BlockNameObject, ManifestItemInterface]>(url);

    if (loading) {
        return <div> Loading data for Hard Skills...</div>
    }

    if (error) {
        return <div>`Error on fetching Hard Skills: ${error}`</div>

    }

    if (!data) {
        return <div>No data on Hard Skills</div>

    }

    const [block_name, data_manifest] = data;

    return (
        <ListGroup>
            <ListGroupItem className="fw-bolder accent">{block_name.block_name}</ListGroupItem>
            <ListGroupItem>{data_manifest.manifest_text}</ListGroupItem>
        </ListGroup>
    )

};

export default ManifestCV;