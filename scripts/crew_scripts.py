from langchain.agents import *
from langchain.tools import tool
from crewai import Crew, Task, Agent


ansible_organizer = Agent(
        role='Ansible Playbook Organizer',
        goal='Organize and improve Ansible playbooks according to best practices',
        backstory='Expert in Ansible playbook optimization and standardization.',
        verbose=True
    )

git_manager = Agent(
        role='Git Repository Manager',
        goal='Manage and maintain the Git repository for playbook version control',
        backstory='Specializes in Git operations and repository management.',
        verbose=True
    )

doc_specialist = Agent(
        role='Documentation Specialist',
        goal='Create and maintain documentation for playbooks and processes',
        backstory='Experienced in technical writing and documentation for software projects.',
        verbose=True
    )

backup_expert=Agent(
        role='Backup and Recovery Expert',
        goal='Develop and implement backup and recovery procedures for playbooks',
        backstory='Skilled in data backup, recovery strategies, and disaster preparedness.',
        verbose=True
    )

def task_organize_playbooks(playbook_directory=str) -> Task:
    return Task(
        description=f'Review and refactor existing Ansible playbooks in {playbook_directory} to align with best practices.',
        agent=ansible_organizer
    )


def task_manage_git()->Task:
    return Task(
        description='Organize the Git repository, implement branch strategies, and ensure proper commit messages.',
        agent=git_manager
    )
def task_create_docs()->Task:
    return Task(
        description='Create and update documentation for playbooks and repository management processes.',
        agent=doc_specialist
    )

def task_backup_plan() ->Task:
    return Task(
        description='Develop a backup strategy and recovery plan for playbooks and repository.',
        agent=backup_expert
    )

def execute_crew(playbook_directory=str) -> str:
    """Execute the crew of agents and tasks. returns a string with the result of the crew's kickoff() method."""
    return Crew(
        agents=[ansible_organizer, git_manager, doc_specialist, backup_expert],
        tasks=[task_organize_playbooks(playbook_directory), task_manage_git(), task_create_docs(), task_backup_plan()],
        verbose=True,
        
    ).kickoff()

