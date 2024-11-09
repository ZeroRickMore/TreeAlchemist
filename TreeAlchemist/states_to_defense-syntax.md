<states>
        <state>
                <description>#any string#</description> <!-- Rule description that will appear on Wazuh dashboard when triggered -->
                <nodes>1,5,8,10</nodes> <!-- Required nodes -->
                <defense id="1"> <!-- The id of the defense you want to map to. This IS one of the <defense id=""> you declared in defense_definition.xml -->
                        <score>#any int#</score> <!-- Unused in backend. Purely for user tracking of what it's being typed. -->
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

