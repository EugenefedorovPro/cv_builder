import React from "react";
import {ListGroup, ListGroupItem} from "react-bootstrap";
import {useFetchData} from "../api/UseFetchData";


interface ProjectItemInterface {
    id: number;
    project_name: string;
    project_text: string;
    web_url: string | null;
    git_url: string | null;

}

type BlockNameType = {
    block_name: string,
}

const Projects = () => {
    const name = "Projects"
    const url: string = "http://localhost:8002/projects/"
    const {data, loading, error} = useFetchData<[BlockNameType, ProjectItemInterface[]]>(url);


    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>`Error on fetching {name}: ${error}`</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }

    const [block_name, projects_data] = data;
    console.log("Project", data);

    return (
        <ListGroup>
            <ListGroupItem className="block-name">
                {block_name.block_name}
            </ListGroupItem>
            {projects_data.map((project) => (
                <ListGroupItem key={project.id} className="projects-items">
                    <div className="title">{project.project_name}</div>
                    <div>{project.project_text}</div>

                    <div>
                        {project?.web_url && (
                            <a href={project.web_url}>web, </a>
                        )}

                        {project?.git_url && (
                            <a href={project.git_url}>git</a>
                        )}

                    </div>

                </ListGroupItem>))}
        </ListGroup>
    )

}

export default Projects