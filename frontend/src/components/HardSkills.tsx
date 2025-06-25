import React from "react";
import {useFetchData} from "../api/UseFetchData";
import {ListGroup, ListGroupItem, Container} from "react-bootstrap";


interface BlockNameObject {
    hard_skills_name: string,
}

interface HardSkillsItemInterface {
    id: number,
    category: string,
    hard_skill_text: string,
}

interface HardSkillsInterface {
    block_names: BlockNameObject;
    hard_skills: HardSkillsItemInterface[];
}

const HardSkillsCV = () => {
    const name = "Hard Skills"
    const url: string = "http://localhost:8002/hard_skills/";
    const {data, loading, error} = useFetchData<HardSkillsInterface>(url);

    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>Error on fetching {name}: {error}</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }

    const {block_names, hard_skills} = data;

    if (!block_names || !hard_skills) {
        return <div>No data on {name}</div>
    }

    return (
        <ListGroup>
            <ListGroupItem className="block-name">{block_names.hard_skills_name}</ListGroupItem>
            {
                hard_skills.map((item) => (
                        <ListGroupItem key={item.id} className="hard-skills-items">
                            <span className="title">{item.category}</span>: {item.hard_skill_text}
                        </ListGroupItem>
                    )
                )
            }
        </ListGroup>
    )
}

export default HardSkillsCV;