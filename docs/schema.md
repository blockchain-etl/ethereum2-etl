# Schema

## beacon_blocks

```
+- beacon_block: record
  |  |- signature: string
  |  +- message: record
  |  |  |- state_root: string
  |  |  |- proposer_index: integer
  |  |  +- body: record
  |  |  |  |- voluntary_exits: string (repeated)
  |  |  |  +- attestations: record (repeated)
  |  |  |  |  |- signature: string
  |  |  |  |  +- data: record
  |  |  |  |  |  +- target: record
  |  |  |  |  |  |  |- root: string
  |  |  |  |  |  |  |- epoch: integer
  |  |  |  |  |  |- beacon_block_root: string
  |  |  |  |  |  +- source: record
  |  |  |  |  |  |  |- root: string
  |  |  |  |  |  |  |- epoch: integer
  |  |  |  |  |  |- index: integer
  |  |  |  |  |  |- slot: integer
  |  |  |  |  |- aggregation_bits: string
  |  |  |  +- proposer_slashings: record (repeated)
  |  |  |  |  +- header_2: record
  |  |  |  |  |  |- signature: string
  |  |  |  |  |  +- message: record
  |  |  |  |  |  |  |- body_root: string
  |  |  |  |  |  |  |- state_root: string
  |  |  |  |  |  |  |- proposer_index: integer
  |  |  |  |  |  |  |- parent_root: string
  |  |  |  |  |  |  |- slot: integer
  |  |  |  |  +- header_1: record
  |  |  |  |  |  |- signature: string
  |  |  |  |  |  +- message: record
  |  |  |  |  |  |  |- body_root: string
  |  |  |  |  |  |  |- state_root: string
  |  |  |  |  |  |  |- proposer_index: integer
  |  |  |  |  |  |  |- parent_root: string
  |  |  |  |  |  |  |- slot: integer
  |  |  |  +- eth1_data: record
  |  |  |  |  |- block_hash: string
  |  |  |  |  |- deposit_count: integer
  |  |  |  |  |- deposit_root: string
  |  |  |  +- attester_slashings: record (repeated)
  |  |  |  |  +- attestation_2: record
  |  |  |  |  |  |- signature: string
  |  |  |  |  |  +- data: record
  |  |  |  |  |  |  +- target: record
  |  |  |  |  |  |  |  |- root: string
  |  |  |  |  |  |  |  |- epoch: integer
  |  |  |  |  |  |  |- beacon_block_root: string
  |  |  |  |  |  |  +- source: record
  |  |  |  |  |  |  |  |- root: string
  |  |  |  |  |  |  |  |- epoch: integer
  |  |  |  |  |  |  |- index: integer
  |  |  |  |  |  |  |- slot: integer
  |  |  |  |  |  |- attesting_indices: integer (repeated)
  |  |  |  |  +- attestation_1: record
  |  |  |  |  |  |- signature: string
  |  |  |  |  |  +- data: record
  |  |  |  |  |  |  +- target: record
  |  |  |  |  |  |  |  |- root: string
  |  |  |  |  |  |  |  |- epoch: integer
  |  |  |  |  |  |  |- beacon_block_root: string
  |  |  |  |  |  |  +- source: record
  |  |  |  |  |  |  |  |- root: string
  |  |  |  |  |  |  |  |- epoch: integer
  |  |  |  |  |  |  |- index: integer
  |  |  |  |  |  |  |- slot: integer
  |  |  |  |  |  |- attesting_indices: integer (repeated)
  |  |  |  +- deposits: record (repeated)
  |  |  |  |  +- data: record
  |  |  |  |  |  |- signature: string
  |  |  |  |  |  |- amount: integer
  |  |  |  |  |  |- withdrawal_credentials: string
  |  |  |  |  |  |- pubkey: string
  |  |  |  |  |- proof: string (repeated)
  |  |  |  |- graffiti: string
  |  |  |  |- randao_reveal: string
  |  |  |- parent_root: string
  |  |  |- slot: integer
  |- root: string
  |- block_timestamp: timestamp
  |- item_type: string
```