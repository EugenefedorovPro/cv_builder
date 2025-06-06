import React from "react";
import {ListGroup, ListGroupItem} from "react-bootstrap";
import {useFetchData} from "../api/UseFetchData";

type BlockNameObject = {
    block_name: string,
}

interface SoftSkillItemInterface {
    id: number;
    soft_skill_text: string;
}

const SoftSkillsCV = () => {
    const name = "Soft Skills"
    const url: string = "http://localhost:8002/soft_skills";
    const {data, loading, error} = useFetchData<[BlockNameObject, SoftSkillItemInterface[]]>(url);

    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>`Error on fetching {name}: ${error}`</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }

    const [block_name, block_data] = data;

    return (
        <>
            <ListGroup>
                <ListGroupItem className="block-name">{block_name.block_name}</ListGroupItem>
            </ListGroup>
            <ListGroup className="soft-skills-items">
                {block_data.map((item) => (
                    <ListGroupItem key={item.id}>{item.soft_skill_text}</ListGroupItem>
                ))}
            </ListGroup>
        </>

    )
}

export default SoftSkillsCV;