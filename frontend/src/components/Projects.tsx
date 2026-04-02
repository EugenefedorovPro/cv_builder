import { urlProjects } from "../urls";
import { ListGroup, ListGroupItem } from "react-bootstrap";
import { useFetchData } from "../api/UseFetchData";
import { ProjectsBlockInterface } from "../components/typesComponents";

const Projects = () => {
  const name = "Projects";
  const { data, loading, error } =
    useFetchData<ProjectsBlockInterface>(urlProjects);

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

  const { projects, block_names } = data;

  if (!projects || !block_names) {
    return <div>No data on {name}</div>;
  }

  return (
    <ListGroup>
      <ListGroupItem className="block-name">
        {block_names.block_names}
      </ListGroupItem>
      {projects.map((project) => (
        <ListGroupItem key={project.id} className="projects-items">
          <div className="title">{project.project_name}</div>
          <div>{project.project_text}</div>

          <div>
            {project?.web_url && <a href={project.web_url}>web,</a>}
            <span> </span>
            {project?.git_url && <a href={project.git_url}>git</a>}
          </div>
        </ListGroupItem>
      ))}
    </ListGroup>
  );
};

export default Projects;
