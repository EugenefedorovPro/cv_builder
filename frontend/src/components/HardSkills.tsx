import React from "react";

interface HardSkillsInterface {
    category: string,
    hard_skills: string,
}

const HardSkillsCV: React.FC<HardSkillsInterface> = (props) => {
    return (
        <div>
            <span>{props.hard_skills}</span>
        </div>
    )
}

export default HardSkillsCV;