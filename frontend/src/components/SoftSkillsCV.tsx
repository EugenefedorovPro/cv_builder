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
    const url: string = "http://localhost:8002/soft_skills";
    const {data, loading, error} = useFetchData<[BlockNameObject, SoftSkillItemInterface[]]>(url);

    if (loading) {
        return <div> Loading data for Hard Skills...</div>
    }

    if (error) {
        return <div>`Error on fetching Hard Skills: ${error}`</div>

    }

    if (!data) {
        return <div>No data on Hard Skills</div>

    }

    const [block_name, block_data] = data;

    return (
        <ListGroup>
            <ListGroupItem className="accent">{block_name.block_name}</ListGroupItem>
            <ul>

                {block_data.map((item) => (
                    <li><ListGroupItem key={item.id}>{item.soft_skill_text}</ListGroupItem></li>
                ))}
            </ul>

        </ListGroup>
    )
}

export default SoftSkillsCV;