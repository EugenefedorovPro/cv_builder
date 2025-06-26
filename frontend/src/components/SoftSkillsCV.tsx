import React from "react";
import {ListGroup, ListGroupItem} from "react-bootstrap";
import {useFetchData} from "../api/UseFetchData";

interface BlockNameInterface {
    soft_skills_name: string,
}

interface SoftSkillItemInterface {
    id: number;
    soft_skill_text: string;
}


interface SoftSkillsBlockInterface {
    soft_skills: SoftSkillItemInterface[];
    block_names: BlockNameInterface;
}

const SoftSkillsCV = () => {
    const name = "Soft Skills"
    const url: string = "http://localhost:8002/soft_skills";
    const {data, loading, error} = useFetchData<SoftSkillsBlockInterface>(url);

    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>`Error on fetching {name}: ${error}`</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }

    const {soft_skills, block_names} = data;

    if (!soft_skills || !block_names) {
        return <div>No data on {name}</div>

    }

    return (
        <>
            <ListGroup>
                <ListGroupItem className="block-name">{block_names.soft_skills_name}</ListGroupItem>
            </ListGroup>
            <ul className="soft-skills-items">
                {soft_skills.map((item) => (
                    <li key={item.id}>{item.soft_skill_text}</li>
                ))}
            </ul>
        </>

    )
}

export default SoftSkillsCV;