SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract GovernanceDAO {
    struct Proposal {
        string description;
        uint256 voteCount;
        bool executed;
    }

    address public admin;
    Proposal[] public proposals;
    mapping(address => bool) public members;
    mapping(uint256 => mapping(address => bool)) public votes;

    modifier onlyMembers() {
        require(members[msg.sender], "Not a DAO member");
        _;
    }

    constructor() {
        admin = msg.sender;
        members[msg.sender] = true;
    }

    function addMember(address member) external {
        require(msg.sender == admin, "Only admin can add members");
        members[member] = true;
    }

    function propose(string calldata description) external onlyMembers {
        proposals.push(Proposal(description, 0, false));
    }

    function vote(uint256 proposalId) external onlyMembers {
        require(!votes[proposalId][msg.sender], "Already voted");
        proposals[proposalId].voteCount++;
        votes[proposalId][msg.sender] = true;
    }

    function execute(uint256 proposalId) external onlyMembers {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.voteCount > 0, "Not enough votes");
        require(!proposal.executed, "Already executed");
        proposal.executed = true;
    }
}


---
