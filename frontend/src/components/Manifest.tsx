import React from "react";
import {ListGroup, ListGroupItem} from "react-bootstrap";
import {useFetchData} from "../api/UseFetchData";

interface BlockNamesInterface {
    block_names: string;
}

interface ManifestItemInterface {
    id: number;
    manifest_text: string;
}

interface ManifestBlockInterface {
    manifest: ManifestItemInterface;
    block_names: BlockNamesInterface;
}

const ManifestCV = () => {
    const name = "Manifest"
    const url: string = "http://localhost:8002/manifest/";
    const {data, loading, error} = useFetchData<ManifestBlockInterface>(url);

    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>Error on fetching {name}: {error}</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }


    const {manifest, block_names} = data;

    if (!manifest || !block_names) {
        return <div>No data on {name}</div>

    }

    return (
        <ListGroup>
            <ListGroupItem><span className="manifest">{manifest.manifest_text}</span></ListGroupItem>
        </ListGroup>
    )

};

export default ManifestCV;