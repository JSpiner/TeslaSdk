// parsing https://developer.tesla.com/docs/fleet-api apis
// run below code and paste to api-spec.json

let codeContent = document.getElementsByClassName('content')[0]

i = 0;
lastSection = null;
sectionGroup = {};
endpoint = null;
scopes = null;
parameters = null;

while (i++ < codeContent.children.length) {
    item = codeContent.children[i];

    // console.log(item)
    if (item.tagName == "H1") {
        section = item.innerHTML;

        console.log("H1 : " + section);
        lastSection = section;
        sectionGroup[lastSection] = {};

        if (section == "FAQ") break;
    }

    else if (lastSection != null && item.tagName == "H2") {
        functionName = item.innerHTML;

        console.log(functionName);
        sectionGroup[lastSection][functionName] = {
            "function": functionName
        };
        endpoint = null;
        scopes = null;
        parameters = null;
    }

    else if (lastSection != null && endpoint == null && item.tagName == "P") {
        endpoint = item.children[0].children[0].innerHTML;
        sectionGroup[lastSection][functionName]['endpoint'] = endpoint;
        console.log("endpoint : " + endpoint);
    }

    else if (endpoint != null && scopes == null && item.tagName == "P") {
        try {
            scopes = item.children[0].innerHTML;
        }
        catch (e) {
            scopes = ""
        }
        sectionGroup[lastSection][functionName]['scopes'] = scopes;
        console.log("scopes : " + scopes);
    }

    else if (scopes != null && parameters == null && item.tagName == "TABLE") {
        tbody = item.children[1];
        parameters = [];
        try {
            for (rowIndex in tbody.children) {
                row = tbody.children[rowIndex].children
                parameters.push(
                    {
                        "name": row[0].innerHTML,
                        "in": row[1].innerHTML,
                        "type": row[2].innerHTML,
                        "required": row[3].innerHTML
                    }
                )
            }
        } catch (e) {

        }
        sectionGroup[lastSection][functionName]['parameters'] = parameters;
        console.log(parameters);
    }


}

console.log("done")
console.log(sectionGroup);
copy(JSON.stringify(sectionGroup));
