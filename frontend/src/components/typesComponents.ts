// Education
export interface EducationBlockNamesInterface {
  education_name: string | null;
}

export interface EducationItemInterface {
  id: number;
  institution: string;
  start_date: string;
  end_date: string;
  degree_title: string;
}

export interface EducationBlockInterface {
  education: EducationItemInterface[];
  block_names: EducationBlockNamesInterface;
}

// Experience
export interface ExperienceBlockNamesInterface {
  experience_name: string | null;
  company_title: string | null;
  exp_period_title: string | null;
  position_title: string | null;
  achievements_title: string | null;
}

export interface ExperienceItemInterface {
  id: number;
  company: string;
  position: string;
  start_date: string;
  end_date: string | null;
  achievements: string | null;
}

export interface ExperienceBlockInterface {
  experience: ExperienceItemInterface[];
  block_names: ExperienceBlockNamesInterface;
}

// HardSkill
export interface HardSkillsBlockNameObject {
  hard_skills_name: string | null;
}

export interface HardSkillsItemInterface {
  id: number;
  category: string;
  hard_skill_text: string;
}

export interface HardSkillsInterface {
  block_names: HardSkillsBlockNameObject;
  hard_skills: HardSkillsItemInterface[];
}

// Header
export interface PhotoInterface {
  photo_url: string;
}

export interface HeaderBlockNamesInterface {
  github_title: string | null;
  linkedin_title: string | null;
  country_title: string | null;
  city_title: string | null;
  district_title: string | null;
}

export interface HeaderInterface {
  id: number;
  first_name: string;
  second_name: string;
  phone: string;
  email: string;
  city: string | null;
  country: string | null;
  district: string | null;
  github: string | null;
  linkedin: string | null;
  photo: PhotoInterface | null;
}

export interface HeaderBlockType {
  header: HeaderInterface;
  block_names: HeaderBlockNamesInterface;
}

// Interest
export interface InterestBlockNameInterface {
  interest_name: string | null;
}

export interface InterestItemInterface {
  id: number;
  interest_text: string;
}

export interface InterestBlockInterface {
  interests: InterestItemInterface[];
  block_names: InterestBlockNameInterface;
}

// Manifest
export interface ManifestBlockNameInterface {
  manifest_name: string | null;
}

export interface ManifestItemInterface {
  id: number;
  manifest_text: string;
}

export interface ManifestBlockInterface {
  manifest: ManifestItemInterface;
  block_names: ManifestBlockNameInterface;
}

// Natural language
export interface NaturalLangBlockNameInterface {
  natural_lang_name: string | null;
}

export interface NaturalLangItemInterface {
  id: number;
  natural_lang: string;
  level: string;
}

export interface NaturalLangBlockInterface {
  natural_langs: NaturalLangItemInterface[];
  block_names: NaturalLangBlockNameInterface;
}

// Projects
export interface ProjectsBlockNameInterface {
  project_name: string | null;
}

export interface ProjectItemInterface {
  id: number;
  project_name: string;
  project_text: string;
  web_url: string | null;
  git_url: string | null;
}

export interface ProjectsBlockInterface {
  projects: ProjectItemInterface[];
  block_names: ProjectsBlockNameInterface;
}

// Soft skills
export interface SoftSkillsBlockNameInterface {
  soft_skills_name: string | null;
}

export interface SoftSkillItemInterface {
  id: number;
  soft_skill_text: string;
}

export interface SoftSkillsBlockInterface {
  soft_skills: SoftSkillItemInterface[];
  block_names: SoftSkillsBlockNameInterface;
}
