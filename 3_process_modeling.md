# Process Modeling

> __PRIMA SLIDE__

## Relevant models

Depending on our purpose

Various types of models can be "drawn" depending on the information we need to analyze

> Difference between process modell and process execution
>
> * Design vs. Execution phase
> * Real world side vs. Computer-readable side
>   * R W: Business process
>   * Porcess executions/Instances
>   * C-R: Business process models
>   * Execution Traces

## Purposes of process modeling

1. Communication
2. Documentation (_clear explanation of our processes_)
3. Analysis (_e.g. simulation_)

## Modeling in BPMN

Can be used for both for conceptual and executable models

### Advantages

* intuitive notation
* improves the communication (_creates standards in communication_)
* improves the analysis

### Core elements

4 types of elements:

* activity (_square box w/ smooth corners_) (verb + noun)
* event (_circles_) (usually named with noun + past-participle verb)
  * start (_light border_)
  * end (_thick border or double border_)
* gateway (_diamond_)
* sequence flow (_black arrow_)
  * a slash on a sequence flow used after a getaway represents the default path when no other condition is met

> The first action in modeling a process involves splitting up the process in his major actions

Time is not a thing, i.e. in gateways there is not time limit, a process will never expire due to time limit => take particular care in and gates

#### Gateways

##### XOR

__XOR-split__ -> takes __one__ outgoing branch

__XOR-join__ -> proceeds when __one__ incoming branch has completed

##### AND

__AND-split__ -> takes __all__ outgoing branches

__AND-join__ -> proceeds when __all__ incoming branches have completed

##### OR

__OR-split__ -> takes __one or more__ branches depending on conditions

__OR-join__ -> proceeds when all __active__ branches have completed

##### Rework ad Repetition

used like a __cycle__ to represent recurring activities that has to be done till an exit condition is met

> Xor-join and And-split have an explicit notation which doesn't involve the diamond

## Process Modelling Viewpoints

* Who
  * Resources
    * Active Resources
      * Process Participants
      * Sofware system
      * Equipment
    * Resource Class
      * [Pool & Lanes](#Pools-&-Lanes)
* What
* When
* Which

### Pools & Lanes

* __Pool__: captures a resource class. Used to model business party
* __Lane__: captures a resource subclass within a pool. Used to model departments