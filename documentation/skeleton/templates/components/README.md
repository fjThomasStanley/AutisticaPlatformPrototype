Components description


# Panel Components
These components are based on core Bootstap components and form the core structural elements of the platform.

## Secondary banner
This component is used to display a tagline to the user, it provides a short description about what the page is about and how the user should be expected to interact with the page

## Jumbotron
This component is used to show key and important information


## Card
This component is used to show key and important information. 

## Expanding Panel
This component is used to contain content in an expandable and collapsible panel. The expanding panel allows the user to hide specific elements of the page if there is too much content being shown.

# Animated Panel Components
These components are animated using javascript to show and hide them. They are core structural elements of the platform.

## Modular Alert 

### Template Inclusion

Template name: imageupload.html 
```
{% include 'pathToComponentTemplate' with modalID=value %} 
```

### Parameters

| Parameter Name   |  Purpose | Requirment | Value |
| :-------------   | :---------- | :-------------   | :---------- |
| ModalID | The unique ID for the component, used by javascript to select component from other components on the page | Required | String - Alphanumeric. As it is an ID, it must be unique to the component. |

### Functions


<table>
        <tr>
            <th>Function Parameter</th>
            <th>Purpose</th>
            <th>Data</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Title of the modular alert</td>
            <td>String - Alphanumeric Text</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Alert text of the modular alert. The body of the modular alert</td>
            <td>String - Alphanumeric Text</td>
        </tr>
        <tr>
            <td>3</td>
            <td>The type of icon displayed in the modular alert</td>
            <td>
                Number:
                <br>
                1 - Alert
                <br>
                2 - Warning
                <br>
                3 - Info
                <br>
                Default value: Warning
            </td>
        </tr>
        <tr>
            <th colspan="3">Example - modular alert component on this page</th>
        </tr>
        <tr>
            <td colspan="3">
                showModularAlert('Timeout Save', 'Inactive for 10 minutes, in 2 minutes time your event will be saved as a draft', 1)
            </td>
        </tr>
        <tr>
            <th colspan="3">Notes</th>
        </tr>
        <tr>
            <td colspan="3">
                The modular alert is a typeof modal component. The modal component requires a modalID to enable the functionality of showing the modal (the modular alert component). Therefore when including the modular alert component within your template you must use the following django tag structure:
                <br>
                <br>
                {{"{% include 'pathToComponentTemplate' with modalID=value %}"}}
            </td>
        </tr>
</table>






## Image Upload

## Accessibility Panel




# Navigation Components
These components are used for platform navigation, they allow the platform user to move around the available sections/pages of the platform and to other related content.

