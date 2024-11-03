<states>
        <state>
                <description>#any string#</description> <!-- Rule description that will appear on Wazuh dashboard when triggered -->
                <nodes>1,5,8,10</nodes> <!-- Required nodes -->
                <defense id="1"> <!-- The id of the defense you want to map to. This IS one of the <defense id=""> you declared in defense_definition.xml -->
                        <optimality-type>BEST_SCORE</optimality-type>
                        <!-- Here all the tags, depending on the chosen <optimality-type> -->
                </defense>
        </state>

</states>



When declaring a defense, utilize the above xml syntax.

## <state>

Each state must be contained within this tag, separatedly

### <nodes>

A list of <node><id>s that you have declared in tree.xml. Every id must be separated by a comma, this way: "1,5,9,10"

### <defense>

#### id

The id of the defense. Must be one of the ones declared in defense_definition.xml in <defense id="{here}">

#### <optimality-type>

Identifier of the type of optimality you want to use. Currently, only "BEST_SCORE" is supported.
Through polymorphism more can be introduces, inheriting from superclass "OptimalityType"

#### extra tags depending on <optimality-type>

##### BEST_SCORE : 
Upon collision, the defense of the HIGHEST <score> wins.
<score> MUST be an integer
NOTE: If <score> is omitted but BEST_SCORE is selected, the default value will be 50.


