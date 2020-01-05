# Example: extra droplets

This example shows how to add other droplets that are not provisioned by this module to the Swarm cluster using output values.

## Running it

You can try out this example by providing a digitalocean access token and running `terraform apply`. Note that you may need to run `terraform init` first.

## Destroying it

Note when destroying, first remove all worker nodes (`count = 0`) before running `terraform destroy`.
