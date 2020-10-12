# Schema

## beacon_blocks.json

```
block_slot: integer
block_epoch: integer
block_timestamp: timestamp
proposer_index: integer
skipped: boolean
block_root: string
parent_root: string 
state_root: string
randao_reveal: string
graffiti: string
eth1_block_hash: string
eth1_deposit_root: string 
eth1_deposit_count: string
signature: string 
attestations: record (repeated) 
|- aggregation_bits: string
|- slot: integer
|- index: integer 
|- beacon_block_root: string
|- source_epoch: integer
|- source_root: string
|- target_epoch: integer
|- target_root: string
|- signature: string
deposits: record (repeated)
|- pubkey: string 
|- withdrawal_credentials: string
|- amount: integer
|- signature: string
proposer_slashings: record (repeated) 
|- header_1_slot: integer 
|- header_1_proposer_index: integer
|- header_1_parent_root: float
|- header_1_state_root: float 
|- header_1_body_root: float
|- header_1_signature: float
|- header_2_slot: integer 
|- header_2_proposer_index: integer
|- header_2_parent_root: float
|- header_2_state_root: float 
|- header_2_body_root: float
|- header_2_signature: float
attester_slashings: record (repeated) 
|- attestation_1_attesting_indices: integer (repeated)
|- attestation_1_slot: integer
|- attestation_1_index: integer 
|- attestation_1_beacon_block_root: string
|- attestation_1_source_epoch: integer
|- attestation_1_source_root: string
|- attestation_1_target_epoch: integer
|- attestation_1_target_root: string
|- attestation_1_signature: string
|- attestation_2_attesting_indices: integer (repeated)
|- attestation_2_slot: integer
|- attestation_2_index: integer 
|- attestation_2_beacon_block_root: string
|- attestation_2_source_epoch: integer
|- attestation_2_source_root: string
|- attestation_2_target_epoch: integer
|- attestation_2_target_root: string
|- attestation_2_signature: string
voluntary_exits: record (repeated)
|- epoch: integer 
|- validator_index: integer
|- signature: string
```

## beacon_blocks.csv

All fields except repeated in [beacon_blocks.json](#beacon_blocksjson). 

Repeated fields will be output to 
`attestations.csv`, 
`deposits.csv`, 
`proposer_slashings.csv`,
`attester_slashings.csv`, 
`voluntary_exits.csv` 
respectively.

## beacon_validators.json

```
pubkey: string
validator_index: integer
balance: integer
withdrawal_credentials: string
effective_balance: integer
slashed: boolean
activation_eligibility_epoch: integer
activation_epoch: integer
exit_epoch: integer
withdrawable_epoch: integer
```

## beacon_validators.csv

Same as [beacon_validators.json](#beacon_validatorsjson).

## beacon_committees.json

```
epoch: integer
epoch_timestamp: timestamp
slot: integer
index: integer
committee: integer (repeated)
```

## beacon_committees.csv

Same as [beacon_committees.json](#beacon_committeesjson). The `committee` field is comma-separated list of integers.